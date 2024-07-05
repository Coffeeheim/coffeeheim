import { useForm } from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import * as yup from 'yup'

const schema = yup
  .object({
    steamid: yup.string().required(),
  })
  .required()

export default function Form() {
  const {
    register,
    handleSubmit,
    setError,
    reset,
    formState: { errors, isSubmitSuccessful, isSubmitting },
  } = useForm({ resolver: yupResolver(schema) })

  const onSubmit = async (data) => {
    const response = await fetch(process.env.REACT_APP_LAMBDA_URL, {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'content-type': 'application/json; charset=utf-8',
      },
    })

    try {
      if (!response.ok) {
        throw new Error(response.status)
      }

      reset()
    } catch (error) {
      setError('steamid', { type: 'custom', message: 'user not found' })
    }
  }

  return (
    <>
      <h2 className="font-semibold text-2xl">Join us</h2>

      <form
        onSubmit={handleSubmit(onSubmit)}
        className="border bg-gray-50 p-5 space-y-2.5 rounded-md lg:w-2/4"
      >
        {isSubmitSuccessful && (
          <p className="bg-green-100 p-2 border border-green-400 text-center">
            Done! The password is{' '}
            <span className="font-semibold bg-yellow-100 font-mono">
              fellowship
            </span>
          </p>
        )}

        <p>
          If you would like to join us on Valheim, submit the following form.
        </p>

        <div>
          <label className="space-y-0.5">
            <div>
              Your steamID64, customURL or complete URL
              <span className="text-sm">
                (
                <a
                  href="https://help.steampowered.com/en/faqs/view/2816-BE67-5B69-0FEC"
                  className="text-indigo-600 underline hover:no-underline"
                  target="_blank"
                  rel="noreferrer"
                >
                  ?
                </a>
                )
              </span>
            </div>
            <input
              className="border border-gray-400 p-2 rounded w-full"
              {...register('steamid')}
            />
            <p className="text-red-600">{errors.steamid?.message}</p>
          </label>
        </div>

        <button
          className="py-2 px-4 text-white bg-indigo-600 rounded disabled:opacity-70"
          disabled={isSubmitting}
        >
          {isSubmitting ? <>Submitting</> : <>Submit</>}
        </button>
      </form>
    </>
  )
}
